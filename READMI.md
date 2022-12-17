 = Dockerfile >> 
 ---
1. FROM python:3.10  *(выбор образа)*

2. RUN mkdir -p /usr/src/app/ *(создание папки)*
3. WORKDIR /usr/src/app/ *(работаем из этой папки)*

4. COPY . /usr/src/app/ \
(Откуда: точка (из нашей машины)\
Куда: /usr/src/app/)  

5. CMD ['python', 'main.py'] (через shell)\
6. ENTRYPOINT ['python', 'main.py'] (без shell)




