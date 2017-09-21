function grad=Calgrad(fun,x)
E=zeros(length(x),1);
grad=zeros(length(x),1);
for i=1:length(x)
    eup=10^(-5);
    E(i)=eup;
    grad(i)=(fun(x+E)-fun(x))/eup;
    E(i)=0;
end
end
