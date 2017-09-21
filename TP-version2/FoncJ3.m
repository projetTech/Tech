function val=FoncJ(x)
% exemple de fonction pour tester l'optimiseur
% fonction avec 4 minima
global dessinpoint
global nb_appel

nb_appel=nb_appel+1;
c1= [-4;-4];
c2= [4;4];
%c3= [6;-4];
c3= [-6;5];
c4= [-6;4];

val1= exp(-0.05*norm(x-c1)^2);
val1= sin(0.1*norm(x-c1));
val2=-exp(-0.08*norm(x-c2)^2);
val3=-0.2*exp(-0.05*norm(x-c3)^2);
val4=-1.2*exp(-0.08*norm(x-c4)^2);

val=val1+val2+val3+val4;

if dessinpoint  % on ne dessine pas les points quand on utilise cette fonction pour les lignes de niveau
plot(x(1),x(2),'or','markersize',14)
hold on
pause(0.1) % pour ralentir un peu
end
