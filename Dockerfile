FROM tiangolo/uwsgi-nginx-flask:python3.6
WORKDIR /app
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ADD . .