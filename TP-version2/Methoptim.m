function [nb_pas_opt, xopt]=Methoptim (critere,x0, methode,eup)
% critère: pointeur su la fontion objectif
% x0 : point de départ pour la convergence
% methode: chaine de caractères décrivant la méthode
%eup=10^(-2);
global nb_pas_opt % comptage du nombre de pas de la méthode
nb_pas_opt=0;
TolX=1e-2; % critère d'arrêt

if  strcmp(methode,'Nelder Matlab') % Nelder et Mead 
    
    options=optimset('TolX',TolX);
    xopt=fminsearch(critere,x0, options);
    
elseif strcmp(methode,'Newton Matlab')% Quasi-Newton 
    
    options=optimset('TolX',TolX,'LargeScale','off');
    xopt= fminunc(critere,x0, options);

    % Méthodes à programmer vous - mêmes: 
    
elseif  strcmp(methode,'Pas Constant') % gradient à pas constant
    rho=0.2;
    x1=x0;
    x2=x0-rho*Calgrad(critere,x0);
    %eup=10^(-10);
    while(critere(x1)>critere(x2)+eup)
        x1=x2;
        x2=x1-rho*Calgrad(critere,x1);
        nb_pas_opt=nb_pas_opt+1;
    end
    xopt=x2;
    % valeur du "pas", à régler 
    % ...... à vous de jouer

elseif strcmp(methode,'Rech Lin') % gradient avec recherche linéaire
    kmax=100;
    %eup=10^(-2);
    k=0;
    x=x0;
    while (norm(Calgrad(critere,x))>eup &&(k<=kmax))
        k=k+1;
        x=Armijo(x,critere(x),-Calgrad(critere,x),Calgrad(critere,x));
        nb_pas_opt=nb_pas_opt+1;
    end
    xopt=x;

 % ..... à vous de jouer  
     
end

% bien penser à renseigner xopt, renvoyé par la fonction


%affichage du nombre de pas d'optimisation le cas écheant
fprintf('nombre de pas d''optim : %u \n', nb_pas_opt)

