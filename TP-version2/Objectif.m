function  J=Objectif(X)
% fonction Objectif
% X contient les coordonnées des points de Steiner 
global xvil lvil lstein
global nappel  % comptage du nombre d'appels 

nappel=nappel+1;  
n=length(X); % dimension de l'espace des X
nbstein=n/2; % nombre de points de Steiner
nbville=size(xvil,2); % nombre de villes (points fixes)
J=0;  % initialisation de J

for ivil=1:nbville  % ajout dans J des distances ville-point de Steiner
    steinvil=lvil(ivil);
    if steinvil~=0
      debstein=2*(steinvil-1)+1;
      J=J+norm(xvil(:,ivil)-X(debstein:debstein+1));
    end
end
for istein=1:nbstein  % ajout dans J des distances points de Steiner entre eux
    steinstein=lstein(istein);
    if steinstein ~= 0
        debstein1=2*(istein-1)+1;
        debstein2=2*(steinstein-1)+1;
        J=J+norm (X(debstein1:debstein1+1)-X(debstein2:debstein2+1));
    end
end

Desgraphe(X) % dessin du graphe ("routes")


