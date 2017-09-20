% programme principal pour détermination de la position des points de
% Steiner

clear all
close all
global xvil lvil lstein
global nappel
nappel=0;
global eup 
eup=10^(-2)
% construction de la structure du réseau en fonction du "cas"
% le point de départ est déterminé dans le "cas"
type_graphe='4villes';
[xvil lvil lstein X0]=Graphe(type_graphe);
% dessin
plot(xvil(1,:),xvil(2,:),'*','linewidth',3)
hold on

% les méthodes ( les deux premières sont déjà installées dans Methoptim)
  %[nb_pas_opt, X]=Methoptim (@Objectif,X0,'Nelder Matlab',eup);
  [nb_pas_opt, X]=Methoptim (@Objectif,X0,'Newton Matlab',eup);
  %[nb_pas_opt, X]=Methoptim (@Objectif,X0,'Pas Constant',eup);
  %[nb_pas_opt, X]=Methoptim (@Objectif,X0,'Rech Lin',eup);
  

 
% Graphique final
plot(xvil(1,:),xvil(2,:),'*','linewidth',3)
hold on
plot(X([1:2:length(X)]),X([2:2:length(X)]),'or','linewidth',3)
title( 'Points de Steiner', 'fontsize',18)
axis equal
grid
% Impression résultats
fprintf('longueur minimale obtenue: %f \n', Objectif(X))
fprintf('nombre d''appels à la fonction objectif: %u \n', nappel)
fprintf('coordonnées des points solution')
X
