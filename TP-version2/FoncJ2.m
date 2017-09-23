function val=FoncJ(x)
% exemple de fonction pour tester l'optimiseur
% en dim 2
global dessinpoint
global nb_appel

nb_appel=nb_appel+1;
A=[1 0 ; 0 0.1];
c1= [-4;-4];
c2= [4;4];
c3= [0;-0];



val1= 20*sin(0.5*norm(x-c1));
val2= (x-c2)'*A*(x-c2);
val3=- 130*exp(-0.05*norm(x-c3)^2);


val=val1+val2+val3;

if dessinpoint  % on ne dessine pas les points quand on utilise cette fonction pour les lignes de niveau
plot(x(1),x(2),'or','markersize',14)
hold on
pause(0.1) % pour ralentir un peu
end
