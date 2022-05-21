# vosk-python-try
VOSKの音声認識を試してみるためのリポジトリ

**build**

```
docker build -t vosk-python-try .
```

**run**
wavディレクトリにファイルをおいて実行

```
docker run --rm --name vosk-python-try -v $(pwd)/src:/src -v $(pwd)/wav:/wav vosk-python-try python wave_sample.py /wav/<filename>
docker run --rm --name vosk-python-try -v $(pwd)/src:/src -v $(pwd)/wav:/wav vosk-python-try python soundfile_sample.py /wav/<filename>
```
