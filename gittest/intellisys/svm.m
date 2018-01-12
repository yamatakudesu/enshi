clear all;
rand('state',0); randn('state',0);
n=200;
a=linspace(0,4*pi,n/2);
u=[a.*cos(a) (a+pi).*cos(a)]'+rand(n,1);
v=[a.*sin(a) (a+pi).*sin(a)]'+rand(n,1);
x=[u v];
y=[ones(1,n/2) -ones(1,n/2)]';
C=1; h=1; hh=2*h^2;

function t = SVM(x,y,C,h,alpha=0.5,beta=0.8)
  [r c] = size(x); 
  epsilon=alpha; 
  hh=h^2;
  t = zeros([r 1]); 
  x2 = diag(x*x');
%ガウスカーネルをまとめたもの
  K = exp(-(repmat(x2,1,r)+repmat(x2',r,1)-2*x*x')/2*hh);
  for k = 1:50
    sum = zeros([200 1]);
    for i = 1:r
      if 1 - y(i) * K(i,:) * t > 0
        sum += y(i)*K(i,:)';
      end
    end
    t = t - epsilon*(C*sum+2*K*t);
    epsilon *= beta;
  end
endfunction

t=SVM(x,y,C,h);
m=100; 
X=linspace(-15,15,m)';
X2=X.^2;
%ノルムを展開してる
U=exp(-(repmat(u.^2,1,m)+repmat(X2',n,1)-2*u*X')/hh);
V=exp(-(repmat(v.^2,1,m)+repmat(X2',n,1)-2*v*X')/hh);
figure(1); clf; hold on; axis([-15 15 -15 15]);
contourf(X,X,sign(V'*(U.*repmat(t,1,m))));
plot(x(y == 1,1),x(y == 1,2),'bo');
plot(x(y == -1,1),x(y == -1,2),'rx');
colormap([1 0.7 1; 0.7 1 1]);





  
