# pyinstaller-package-specification

该项目记录 python 打包成二进制文件的方法和范例。

## TLDR


打包应用程序很容易，但连同数据文件一起打包很麻烦，简而言之，使用如下命令打包 app.py，pyinstaller 会根据 app.py 中的 `import` 自动分析依赖。如果 app.py 中操作了 `sys.path`，pyinstaller 不能识别，所以需要需要手动导入。


解释：

`--add-data="data/*;data`: 将 data 目录下的所有文件放到打包后的程序的 data 目录下。在 UNIX 中将 `;` 改为 `:`。
`--nocnfirm`：如果之前已经打包过，再次打包会提示是否删除之前的打包好的程序，使用该选项将自动删除。
`--noupx`：upx 会压缩动态链接库，不建议压缩，经常会导致程序无法正常运行。
`--windowed`：以窗口模式运行，即不显示命令行。通常在调试的时候会省略该选项，方便显示调试信息。发布应用的时候应该加上该选项，以隐藏命令行。

除了执行该命令，还有对要打包的数据，还有代码稍作修改。

1. 在要打包的数据木下创建 `__init__.py`，将值看作为一个 Python 模块
2. 在主程序代码中导入 pkgutil 模块，用 pkgutil(<module_name>, <file_name)>) 导入文件，如果文件是文本，还需要用 decode 解码。

```python
import pkgutil

text_txt = pkgutil.get_data( 'data', 'text.txt' ) # text_txt 是二进制文件
text = text_txt.decode('utf-8') # text 通过解码获得
```

### 使用 pyinstaller 打包

`pyinstaller --add-data="data/*;data"  --noconfirm --onefile  --noupx --windowed app.py `


## 注意事项

为什么会有上面这么麻烦的打包方式，直接在程序中使用相对路径读取打包好的数据文件路径不可以吗？确实不可行。

--onedir 模式下，可以正常打包 data 文件，但在 --onefile 下，会出现找不到数据文件的情况。
