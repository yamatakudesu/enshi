clear all;
rand('state', 0); randn('state', 0);
n = 50; N = 1000;
x=linspace(-3, 3, n)'; X=linspace(-3, 3, N)';
pix=pi*x;
y = sin(pix)./(pix) + 0.1*x + 0.2*randn(n,1);
truey = sin(pix)./(pix) + 0.1*x

x2=x.^2;
xx=repmat(x2,1,n)+repmat(x2',n,1)-2*x*x';
hhs=2*[0.001 0.01 0.1 1 10].^2; ls=[0.001 0.01 0.1 1 10];

m=5; u=floor(m*[0:n-1]/n)+1; u=u(randperm(n));
for hk=1:length(hhs)
    hh=hhs(hk); k=exp(-xx/hh);
    for i=1:m
        ki=k(u~=i,:); kc=k(u==i,:); yi=y(u~=i); yc=y(u==i);
        for lk=1:length(ls)
            l=ls(lk); t=(ki'*ki+l*eye(n))\(ki'*yi); fc=kc*t;
            g(hk,lk,i)=mean((fc-yc).^2);
        end
    end
end
mean(g,3)
[gl,ggl]=min(mean(g,3),[],2); [ghl, gghl]=min(gl);
L=ls(ggl(gghl)); HH=hhs(gghl); H=(HH/2)**0.5;

H, L

K=exp(-(repmat(X.^2,1,n)+repmat(x2',N,1)-2*X*x')/HH);
k=exp(-xx/HH);
t=(k^2+L*eye(n))\(k*y);
F=K*t;

figure(1); clf; hold on; axis([-2.8 2.8 -1 1.5]);
plot(X, F, 'g-');
plot(x, truey, 'r-');
plot(x, y, 'bo');
