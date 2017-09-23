eup=10^(-3):0.0001:10^(-1);
nbIterVector=zeros(length(eup));
nbappelVector=zeros(length(eup));
for i=1:length(eup)
    [nbIterVector(i),nbappelVector(i)]=Performance(eup(i));
    
end 
figure()
subplot(1,2,1)
plot(eup,nbIterVector)
subplot(1,2,2)
plot(eup,nbappelVector)
%ajouter le temps 
