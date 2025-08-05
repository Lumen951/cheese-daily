#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简单的HTTP服务器来运行Dify前端应用
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def run_server(port=8000):
    """启动HTTP服务器"""
    # 切换到前端目录
    frontend_dir = Path(__file__).parent
    os.chdir(frontend_dir)
    
    # 创建服务器
    with socketserver.TCPServer(("", port), CORSHTTPRequestHandler) as httpd:
        print(f"🚀 服务器启动成功!")
        print(f"📱 请在浏览器中访问: http://localhost:{port}")
        print(f"📁 服务目录: {frontend_dir}")
        print(f"🔑 Dify API: http://localhost/v1")
        print(f"⏹️  按 Ctrl+C 停止服务器")
        print("-" * 50)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 服务器已停止")
            httpd.shutdown()

if __name__ == "__main__":
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("❌ 端口号必须是数字")
            sys.exit(1)
    
    run_server(port) 