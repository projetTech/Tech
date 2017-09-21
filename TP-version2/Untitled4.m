x=0:0.1:5;
for i=1:length(x)
    GradAnal(i)=(2*x(i));
  
    A(i)=Calgrad(@f,x(i));
end



plot(x,A,'r')
hold on 
plot(x,GradAnal,'b')
title('courbes du gradien analytique et de ma fonction Calgrad')
xlabel('x')
ylabel('gradient')
