function x=Armijo(x0,Jx0,d0,Grad)
% recherche monodim par une méthode d'Armijo simple
% x0 point d'où part la recherche
% Jx0: valeur de J en x0
% d0: direction de recherche, qui n'est pas -Grad dans le cas du gradient
% conjugué
% Grad: Gradient de J en x0 

% x: retourne le point choisi comme ayant réalisé une descente sufisante
% ici on diminue le premier pas et la pente quand on s'approche de la solution*
%( multiplication par norm(Grad))

% -----------------------------------
% parametres de réglage: essayer de les améliorer, de gérer leur variations
% (fonction du gradient? autre idée?)
%alpha=0.3*norm(Grad);  %  taille premier pas, celui ci va bien pour Steiner 
alpha=2;    % celui-là pour les tests sur les fonctions J1, J2, J3 . Mais essayer d'améliorer

epsi=0.2;    % essayer aussi = 0.05*norm(Grad);   %  pourcentage de la pente
beta=4;      % pour division du pas, retour en arriere si trop loin

% --------------------------------------



d0=d0/norm(d0);% vecteur unitaire de la droite de descente
pente=epsi*Grad'*d0; % 
nonstop=1;
ncoups=0;
while and(nonstop==1,ncoups<10)
 ncoups=ncoups + 1;
 x=x0+alpha*d0;
 dessous=Objectif(x)-(Jx0+alpha*pente);
 if dessous<0
     nonstop=0; % on est dans la zone acceptable
 else
     alpha=alpha/beta;% on est trop loin
 end
    
end
