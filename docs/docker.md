# Docker Engine配置
添加国内镜像源加速镜像下载
{
  "builder": {
    "gc": {
      "defaultKeepStorage": "20GB",
      "enabled": true
    }
  },
  "experimental": false,
  "registry-mirrors":[
    "https://docker.m.daocloud.io",
    "https://docker.rainbond.cc",
    "https://docker.lmirror.top"
]
}

