function [nbIter,nappel]=Performance(eup)
%     global xvil lvil lstein
    global nb_pas_opt 
    global nappel
    nappel=0;
%     global eup 
    % construction de la structure du réseau en fonction du "cas"
    % le point de départ est déterminé dans le "cas"
%     type_graphe='3villes';
%      [xvil lvil lstein X0]=Graphe(type_graphe);
%     % dessin
%     plot(xvil(1,:),xvil(2,:),'*','linewidth',3)
%     hold on
X0=[0.8;0.8 ];
    % les méthodes ( les deux premières sont déjà installées dans Methoptim)
      %[nb_pas_opt, X]=Methoptim (@Objectif,X0,'Nelder Matlab',eup);
      %[nb_pas_opt, X]=Methoptim (@Objectif,X0,'Newton Matlab',eup);
      [nb_pas_opt, X]=Methoptim (@Objectif,X0,'Pas Constant',eup);
%       [nb_pas_opt, X]=Methoptim (@Objectif,X0,'Rech Lin',eup);



    % % Graphique final
    % plot(xvil(1,:),xvil(2,:),'*','linewidth',3)
    % hold on
    % plot(X([1:2:length(X)]),X([2:2:length(X)]),'or','linewidth',3)
    % title( 'Points de Steiner', 'fontsize',18)
    % axis equal
    % grid
    % Impression résultats
%     fprintf('longueur minimale obtenue: %f \n', Objectif(X))
%     fprintf('nombre d''appels à la fonction objectif: %u \n', nappel)
%     fprintf('coordonnées des points solution')
%     X
    nbIter=nb_pas_opt;
