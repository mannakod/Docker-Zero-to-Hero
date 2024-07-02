FROM nginx:latest

RUN apt-get update && \
    apt install rtorrent megatools -y && \
    apt install openssh-server  -y && \
    apt install nano -y && \
    apt-get clean 


WORKDIR /root/

COPY index.html /usr/share/nginx/html/
COPY pubkey /root/


RUN mkdir /run/sshd    
RUN mkdir -p ~/.ssh
RUN cat /root/pubkey >> ~/.ssh/authorized_keys

RUN echo 'Port 22' >> /etc/ssh/sshd_config && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config


EXPOSE 80
EXPOSE 22
CMD ["nginx", "-g", "daemon off;"]
CMD ["/usr/sbin/sshd", "-D"]
