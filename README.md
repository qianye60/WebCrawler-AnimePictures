# 🌸 Anime-Pictures 爬虫：二次元美图，触手可及！🌸

[![GitHub stars](https://img.shields.io/github/stars/qianye60/WebCrawler-AnimePictures.svg?style=social&label=Star&maxAge=2592000)](https://github.com/qianye60/WebCrawler-AnimePictures/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/qianye60/WebCrawler-AnimePictures.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/qianye60/WebCrawler-AnimePictures/network/)
[![GitHub license](https://img.shields.io/github/license/qianye60/WebCrawler-AnimePictures.svg)](https://github.com/qianye60/WebCrawler-AnimePictures/blob/master/LICENSE)

## 🌟 项目简介

还在为寻找心仪的动漫美图而烦恼吗？Anime-Pictures 爬虫，基于 Python 和 DrissionPage 库，为您打造专属二次元图库！🚀

本项目专为 [Anime-Pictures.net](https://anime-pictures.net/) 设计，让您轻松爬取海量高质量动漫图片。无论是壁纸控，还是图库收集爱好者，它都能满足您的需求！

### ✨ 特色功能

*   **🎯 精准定位**：支持关键词、排除标签、排序方式、发布时间等多维度筛选，想爬什么就爬什么！
*   **⚙️ 高级设置**：自定义每页图片数量，灵活控制爬取速度。
*   **📈 断点续爬**：支持从上次中断处继续，省时省力。
*   **💾 自动保存**：图片自动下载至 `pictures` 文件夹，方便管理。
*   **📝 参数配置**：首次使用引导设置，参数自动保存，一劳永逸。

## 🛠️ 环境准备

1.  **Python 环境**：确保已安装 Python 3.6 或更高版本。
2.  **Chromium 浏览器**：DrissionPage 会自动下载并管理 Chromium 浏览器，无需手动安装。

## 📦 安装依赖

```bash
pip install DrissionPage
```

## 🚀 快速开始

1.  **克隆项目**：

    ```bash
    git clone https://github.com/qianye60/WebCrawler-AnimePictures.git
    cd 您的仓库名
    ```

2.  **运行爬虫**：

    ```bash
    python WebCrawler(AnimePictures).py
    ```

3.  **根据提示输入**：

    *   首次使用，请根据提示设置账号密码、每页张数、爬取标签等参数。
    *   后续使用，程序将自动读取上次的配置。

## ⚙️ 代码结构

*   `WebCrawler(AnimePictures).py`：爬虫主程序。
*   `pictures` 文件夹：用于存储下载的图片。
*   `C:\\Users\\Public\\setting.json`:自动生成的配置文件
## 📝 使用说明

### `class picture`

核心爬虫类，包含以下方法：

*   `__init__(self, setlist)`：初始化爬虫对象。
    *   `setlist`：包含所有配置参数的字典。
*   `login_set(self)`：处理用户登录和设置每页图片数量。
*   `crawler(self)`：爬取图片的核心逻辑。
    *   根据 `setlist` 中的参数构建 URL。
    *   循环爬取每一页的图片。
    *   进入每张图片的详情页，点击下载按钮。
    *   等待下载开始和结束，并记录下载进度。
    *   将配置参数写入到文件中
*   `start(self)`：启动爬虫，先调用 `login_set`，再调用 `crawler`。

## 💡 进阶玩法

*   **自定义搜索关键词**：修改 `setlist` 中的 `search_tag` 参数。
*   **排除特定标签**：修改 `setlist` 中的 `denied_tag` 参数。
*   **调整排序方式**：修改 `setlist` 中的 `order_by` 参数。
*   **筛选发布时间**：修改 `setlist` 中的 `ldate` 参数。
*   **定时任务**：结合操作系统的定时任务功能（如 Linux 的 cron），实现定期自动爬取。

##  注意事项

*   请尊重网站的 robots.txt 协议，合理控制爬取频率，避免对服务器造成过大压力。
*   如果觉得慢可自行降低等待速度，但是可能会导致爬取失败。
*   爬取到的图片仅供个人学习、欣赏使用，请勿用于商业用途。
*   本项目仅供学习交流，开发者不对任何滥用行为负责。

## 🤝 贡献代码

欢迎提交 Pull Request，一起完善这个项目！

## 📜 开源协议

本项目采用 MIT 许可证，详情请参见 [LICENSE](LICENSE) 文件。

---

**觉得好用的话，别忘了给个 Star 哦！** ⭐
