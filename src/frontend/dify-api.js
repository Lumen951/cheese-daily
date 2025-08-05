// Dify API 集成模块
class DifyAPI {
    constructor(apiKey, apiUrl) {
        this.apiKey = apiKey;
        this.apiUrl = apiUrl;
    }

    // 上传文件到 Dify
    async uploadFile(file, user = "web_user") {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('user', user);
        
        // 根据文件类型设置正确的type参数
        let fileType = "TXT";
        if (file.type === 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' || 
            file.type === 'application/vnd.ms-excel') {
            fileType = "XLSX";
        } else if (file.type === 'text/csv' || file.type === 'application/csv') {
            fileType = "CSV";
        }
        formData.append('type', fileType);

        try {
            console.log(`上传文件中... 类型: ${fileType}`);
            const response = await fetch(`${this.apiUrl}/files/upload`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`
                },
                body: formData
            });

            if (response.status === 201) {
                console.log("文件上传成功");
                const result = await response.json();
                return result.id; // 返回文件ID
            } else {
                throw new Error(`文件上传失败: ${response.status} - ${response.statusText}`);
            }
        } catch (error) {
            console.error('文件上传错误:', error);
            throw error;
        }
    }

    // 运行工作流
    async runWorkflow(fileIds, user = "web_user", responseMode = "blocking") {
        const payload = {
            inputs: {
                orig_mail: fileIds.map(fileId => ({
                    transfer_method: "local_file",
                    upload_file_id: fileId,
                    type: "document"
                }))
            },
            response_mode: responseMode,
            user: user
        };

        try {
            console.log("运行工作流...");
            const response = await fetch(`${this.apiUrl}/workflows/run`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (response.status === 200) {
                console.log("工作流执行成功");
                return await response.json();
            } else {
                throw new Error(`工作流执行失败: ${response.status} - ${response.statusText}`);
            }
        } catch (error) {
            console.error('工作流执行错误:', error);
            throw error;
        }
    }

    // 发送聊天消息（保留原有方法以兼容）
    async sendChatMessage(query, files = [], inputs = {}) {
        const payload = {
            inputs: {
                ...inputs,
                files: files.map(file => ({
                    name: file.name,
                    size: file.size,
                    type: file.type,
                    content: file.content || null
                }))
            },
            query: query,
            response_mode: "blocking",
            user: "web_user"
        };

        try {
            const response = await fetch(`${this.apiUrl}/chat-messages`, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });

            if (!response.ok) {
                throw new Error(`API 请求失败: ${response.status} - ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error('Dify API 错误:', error);
            throw error;
        }
    }



    // 获取工作流状态
    async getWorkflowStatus(messageId) {
        try {
            const response = await fetch(`${this.apiUrl}/messages/${messageId}`, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${this.apiKey}`,
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error(`获取状态失败: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('获取状态错误:', error);
            throw error;
        }
    }
}

// 文件处理工具
class FileProcessor {
    static async readFileAsText(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = (e) => resolve(e.target.result);
            reader.onerror = (e) => reject(e);
            reader.readAsText(file);
        });
    }

    static async readFileAsBase64(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = (e) => resolve(e.target.result);
            reader.onerror = (e) => reject(e);
            reader.readAsDataURL(file);
        });
    }

    static formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    static validateFile(file) {
        const allowedTypes = [
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', // .xlsx
            'application/vnd.ms-excel', // .xls
            'text/csv', // .csv
            'application/csv' // 某些系统可能使用这个MIME类型
        ];

        const maxSize = 10 * 1024 * 1024; // 10MB

        if (!allowedTypes.includes(file.type)) {
            throw new Error(`不支持的文件类型: ${file.type}。仅支持 Excel (.xlsx, .xls) 和 CSV (.csv) 格式`);
        }

        if (file.size > maxSize) {
            throw new Error(`文件大小超过限制: ${this.formatFileSize(maxSize)}`);
        }

        return true;
    }
}

// 导出模块
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { DifyAPI, FileProcessor };
} 