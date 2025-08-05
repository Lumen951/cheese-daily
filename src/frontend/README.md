# Dify 工作流前端应用

这是一个基于 Dify API 的现代化前端应用，允许用户通过网页界面上传文件并启动 AI 工作流。

## 🚀 功能特性

- **现代化UI设计**: 使用奇绩蓝 (#0884ff) 作为主色调
- **拖拽文件上传**: 支持拖拽和点击上传文件
- **多文件支持**: 可以同时上传多个文件
- **文件验证**: 自动验证文件类型和大小
- **实时反馈**: 显示上传进度和处理状态
- **响应式设计**: 适配各种屏幕尺寸

## 📁 文件结构

```
src/frontend/
├── index.html          # 主页面文件
├── dify-api.js        # Dify API 集成模块
├── server.py          # 本地服务器
└── README.md          # 说明文档
```

## 🛠️ 安装和运行

### 方法一：使用 Python 服务器（推荐）

1. 确保已安装 Python 3.6+
2. 在终端中运行：

```bash
cd src/frontend
python server.py
```

3. 在浏览器中访问：`http://localhost:8000`

### 方法二：使用其他 HTTP 服务器

如果您的系统有其他 HTTP 服务器，也可以直接使用：

```bash
# 使用 Node.js http-server
npx http-server src/frontend -p 8000

# 使用 Python 内置服务器
cd src/frontend
python -m http.server 8000
```

## ⚙️ 配置说明

### Dify API 配置

在 `index.html` 文件中，您可以修改以下配置：

```javascript
const DIFY_API_KEY = 'app-Zk1QgpWmbh2iwdvzRzBC256m';  // 您的 Dify API 密钥
const DIFY_API_URL = 'https://api.dify.ai/v1';         // Dify API 服务器地址
```

### API 调用流程

1. **文件上传**: 使用 `/files/upload` 端点上传文件
2. **工作流执行**: 使用 `/workflows/run` 端点执行工作流
3. **文件类型支持**: 
   - Excel 文件: `XLSX` 类型
   - CSV 文件: `CSV` 类型

### 支持的文件类型

- Excel 文件 (.xlsx, .xls)
- CSV 文件 (.csv)

**文件大小限制**: 10MB

## 🎨 界面特性

### 主色调
- 奇绩蓝: `#0884ff`
- 渐变效果: 从 `#0884ff` 到 `#0666cc`

### 交互效果
- 拖拽上传区域悬停效果
- 按钮点击动画
- 加载动画
- 错误提示

## 🔧 自定义配置

### 修改支持的文件类型

在 `dify-api.js` 文件中修改 `FileProcessor.validateFile()` 方法：

```javascript
static validateFile(file) {
    const allowedTypes = [
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', // .xlsx
        'application/vnd.ms-excel', // .xls
        'text/csv', // .csv
        'application/csv' // 某些系统可能使用这个MIME类型
        // 添加更多文件类型
    ];
    // ...
}
```

### 修改文件大小限制

```javascript
const maxSize = 10 * 1024 * 1024; // 10MB
```

## 🐛 故障排除

### 常见问题

1. **CORS 错误**
   - 确保 Dify API 服务器允许跨域请求
   - 检查 API 服务器地址是否正确

2. **文件上传失败**
   - 检查文件类型是否支持
   - 确认文件大小未超过限制
   - 验证网络连接

3. **API 请求失败**
   - 确认 API 密钥正确
   - 检查 API 服务器是否运行
   - 验证 API 端点是否正确

### 调试模式

在浏览器开发者工具中查看控制台输出，获取详细的错误信息。

## 📝 开发说明

### 添加新功能

1. 在 `dify-api.js` 中添加新的 API 方法
2. 在 `index.html` 中集成新功能
3. 更新样式和交互逻辑

### 样式修改

所有样式都在 `index.html` 的 `<style>` 标签中，可以直接修改。

## 📄 许可证

本项目基于 MIT 许可证开源。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！ 