function Desgraphe(X)
global xvil lvil lstein

n=length(X);
nbstein=n/2;
nbville=size(xvil,2);

plot(xvil(1,:),xvil(2,:),'*','linewidth',3)
hold on

for ivil=1:nbville
    steinvil=lvil(ivil);
    if steinvil~=0
      debstein=2*(steinvil-1)+1;
      plot([xvil(1,ivil);X(debstein)],[xvil(2,ivil);X(debstein+1)],'linewidth',2)
      hold on
    end
end
for istein=1:nbstein
    steinstein=lstein(istein);
    if steinstein ~=0
        debstein1=2*(istein-1)+1;
        debstein2=2*(steinstein-1)+1;
        plot([X(debstein1),X(debstein2)],[X(debstein1+1),X(debstein2+1)],'linewidth',2 )
        hold on
    end
end
axis equal
hold off
pause(0.2)

