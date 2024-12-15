import tkinter as tk
import requests
from tkinter import messagebox, ttk
import os
import subprocess
from threading import Thread

class IDEInstaller:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("程序员常用软件安装器（安装包保存路径：C:/IDE）")
        self.window.geometry("600x800")
        
        # IDE下载链接字典
        self.ide_links = {
            "Python3.14.0": "https://mirrors.aliyun.com/python-release/windows/python-3.14.0a2.exe",
            "Dev-Cpp": "https://softdl.360tpcdn.com/auto/20180710/104870_581d2ec5eff634a610705d01ec6da553.exe?channel=4016227",
            "IntelliJ IDEA": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/apps/adp/pkg/3002-2024-11-18053040-1731922240824.exe?sign=333dee2eb52afed5d048abbfaf59f2a4&t=6760f081&order=0&uuid=f9d98df583224bbba7845673876e3dca&cMD5=false&sorder=0&group=&ts=1734233473818&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "Visual Studio Code": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/normal/apps/4380-2024-12-12094949-1733968189326.exe?sign=d213f7991ed1d7a51b5e14e5112f6e69&t=6760f0a6&order=0&uuid=5b4932b0ed6c4de5a3e8dfa553b7b4a7&cMD5=false&sorder=0&group=&ts=1734233510365&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "Visual Studio 2019": "https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=16",
            "PyCharm": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/apps/adp/pkg/1093-2024-11-18053209-1731922329115.exe?sign=08d409358f0490974118c2b528c0f259&t=6760f153&order=0&uuid=2ce9842b2eb844b2b57b58c0de53a89b&cMD5=false&sorder=0&group=&ts=1734233683667&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "PhpStorm": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/normal/apps/7743-2021-05-27112907-1622086147713.exe?sign=7b2becac1e04c35b0f6cc944c95cda50&t=6760f174&order=0&uuid=a186975f322b48d38ea5ca3a51454397&cMD5=false&sorder=0&group=&ts=1734233716980&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "GoLand": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/apps/adp/pkg/8702-2024-11-22032025-1732260025996.exe?sign=5da9eba59abcedf958397082d373cb6a&t=6760f1c4&order=0&uuid=25cf124827dc4a7b93da6eb56b8f99ca&cMD5=false&sorder=0&group=&ts=1734233796460&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "Rider": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/apps/adp/pkg/5628-2024-11-22032347-1732260227425.exe?sign=9710886b6d49492397d3a72fb7f50037&t=6760f203&order=0&uuid=584e2b5596424d3d977fde6a4224b0df&cMD5=false&sorder=0&group=&ts=1734233859633&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "CLion": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/normal/apps/6552-2022-12-06044454-1670316294648.exe?sign=627325def808be611c08e8e788c9b11f&t=6760f247&order=0&uuid=4620a513cfa44c9eb4ec42037734f8c4&cMD5=false&sorder=0&group=&ts=1734233927561&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "RustRover": "https://download.jetbrains.com/rustrover/RustRover-2023.1.exe",
            "WebStorm": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/apps/adp/pkg/2052-2024-11-22032134-1732260094684.exe?sign=cfe7bc9e09a59c92deaee6cf61bf271f&t=6760f493&order=0&uuid=c3075529d33b446b9372c19aa01a62a2&cMD5=false&sorder=0&group=&ts=1734234515045&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "RubyMine": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/normal/apps/3478-2020-03-18093112-1584495072692.exe?sign=8ebb4641a15aa55e2f250a32260fa051&t=6760f4dc&order=0&uuid=d517b6e8062c413181ffdfddbbe79ddb&cMD5=false&sorder=0&group=&ts=1734234588231&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "DataGrip": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/normal/apps/6978-2022-12-06043809-1670315889663.exe?sign=ce0b262fb3675a847b10164e214d909d&t=6760f4f7&order=0&uuid=8be8b199ab6745c781675856c52ac167&cMD5=false&sorder=0&group=&ts=1734234615600&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "ReSharper": "https://pc-lsw7.lenovomm.cn/dlserver/fileman/pcstore/ali/pcsd-pcmgr-appstore/appstore/normal/apps/5940-2020-03-18090527-1584493527395.exe?sign=ccde0b097f1a646dc0e7698052a306a1&t=6760f52e&order=0&uuid=69930428867f4cae830f124e460777fb&cMD5=false&sorder=0&group=&ts=1734234670593&cpn=-1&cid=8848&__bc=10101&__cid=8848&__ip=0.0.0.0&__ept=1&dck=1",
            "Aqua": "https://download.jetbrains.com/aqua/aqua-2023.1.exe"
        }
        
        # 创建下载目录
        self.download_dir = "C:/IDE"
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)
            
        # 添加进度条框架
        self.progress_frames = {}
        
        # 添加需要特殊提示的IDE列表
        self.paid_ide = ["GoLand"]
        self.no_cn_source = ["RustRover", "Aqua"]
        
        self.create_buttons()
        
    def create_buttons(self):
        """创建所有IDE的安装按钮和对应的进度条"""
        for i, (ide_name, _) in enumerate(self.ide_links.items()):
            # 为每个IDE创建一个框架来容纳按钮和进度条
            frame = tk.Frame(self.window)
            frame.grid(row=i, column=0, padx=10, pady=5, sticky='ew')
            
            btn = tk.Button(
                frame,
                text=f"安装 {ide_name}",
                width=30,
                command=lambda name=ide_name: self.start_download(name)
            )
            btn.pack(side=tk.LEFT, padx=5)
            
            # 创建进度条
            progress = ttk.Progressbar(
                frame,
                length=200,
                mode='determinate',
                style='TProgressbar'
            )
            progress.pack(side=tk.LEFT, padx=5)
            
            # 创建进度标签
            progress_label = tk.Label(frame, text="0%")
            progress_label.pack(side=tk.LEFT, padx=5)
            
            # 保存进度条和标签的引用
            self.progress_frames[ide_name] = {
                'bar': progress,
                'label': progress_label
            }
            
    def download_file(self, ide_name, url):
        """下载文件的具体实现，带进度显示"""
        try:
            response = requests.get(url, stream=True)
            file_name = os.path.join(self.download_dir, f"{ide_name}.exe")
            
            # 获取文件总大小
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024  # 1 Kibibyte
            downloaded = 0
            
            with open(file_name, 'wb') as f:
                for data in response.iter_content(block_size):
                    if data:
                        f.write(data)
                        downloaded += len(data)
                        # 计算下载进度
                        if total_size:
                            progress = (downloaded / total_size) * 100
                            # 使用after方法在主线程中更新进度条
                            self.window.after(
                                0,
                                self.update_progress,
                                ide_name,
                                progress
                            )
            
            # 下载完成后运行安装程序
            subprocess.Popen(file_name)
            messagebox.showinfo("成功", f"{ide_name} 下载完成并开始安装")
            
        except Exception as e:
            messagebox.showerror("错误", f"下载 {ide_name} 时发生错误：{str(e)}")
        finally:
            # 重置进度条
            self.window.after(0, self.reset_progress, ide_name)
            
    def update_progress(self, ide_name, progress):
        """更新进度条和标签"""
        progress_frame = self.progress_frames.get(ide_name)
        if progress_frame:
            progress_frame['bar']['value'] = progress
            progress_frame['label'].config(text=f"{progress:.1f}%")
            
    def reset_progress(self, ide_name):
        """重置进度条和标签"""
        progress_frame = self.progress_frames.get(ide_name)
        if progress_frame:
            progress_frame['bar']['value'] = 0
            progress_frame['label'].config(text="0%")
            
    def start_download(self, ide_name):
        """开始下载进程，增加特殊提示"""
        if ide_name in self.paid_ide:
            if not messagebox.askyesno("警告", 
                "警告：GoLand暂无免费社区版，是否确定下载？",
                icon='warning'):
                return
                
        if ide_name in self.no_cn_source:
            if not messagebox.askyesno("警告",
                "警告：此应用暂未找到国内源，是否确定下载？",
                icon='warning'):
                return
        
        url = self.ide_links[ide_name]
        messagebox.showinfo("开始下载", f"开始下载 {ide_name}，请稍候...")
        # 在新线程中进行下载，避免界面卡顿
        download_thread = Thread(target=self.download_file, args=(ide_name, url))
        download_thread.start()
        
    def run(self):
        """运行程序"""
        self.window.mainloop()

if __name__ == "__main__":
    app = IDEInstaller()
    app.run()
