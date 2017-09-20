function val=EFoncJ(x)
% exemple de fonction quadratique simple pour tester  l'optimiseur

global dessinpoint
global nb_appel

nb_appel=nb_appel+1;

A=[ 1  0.3 ; 0.3, 3];
b= [5;0];
val=(x)'*A*(x);

if dessinpoint  % on ne dessine pas les points quand on utilise cette fonction pour les lignes de niveau
plot(x(1),x(2),'or','markersize',14)
hold on
pause(0.1) % pour ralentir un peu
end
