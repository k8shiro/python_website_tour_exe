# python_website_tour_exe


## 開発用
**linux向けコマンド**

```
docker build  -f ./linux/Dockerfile -t python-website-tour-exe-linux .
docker run --rm -it python-website-tour-exe-linux bash

docker run --rm -v $(pwd)/src:/src -v $(pwd)/linux:/linux \
    python-website-tour-exe-linux pyinstaller main.py \
    --onedir --onefile --clean \
    --distpath /linux/dist \
    --workpath /linux/build \
    --specpath /linux 
```

**centos7向けコマンド**

```
docker build  -f ./centos7/Dockerfile -t python-website-tour-exe-centos7 .
docker run --rm -it -v $(pwd)/src:/src python-website-tour-exe-centos7 bash

docker run --rm -v $(pwd)/src:/src -v $(pwd)/centos7:/centos7 \
    python-website-tour-exe-centos7 pyinstaller main.py \
    --onedir --onefile --clean \
    --distpath /centos7/dist \
    --workpath /centos7/build \
    --specpath /centos7 
```

**windows向けコマンド**

```

```