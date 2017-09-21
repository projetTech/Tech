% Test de la fonction Methoptim

clear all
close all
global nb_pas_opt 
global nb_appel
global dessinpoint

% nom des méthodes 'Nelder Matlab' 'Newton Matlab''Pas Constant''Rech Lin'

FoncCout=@FoncJ2;   % fonction à optimiser (2D)
dessinpoint= false;
DessinTest(FoncCout)
x0=(ginput (1))';
plot(x0(1),x0(2),'or','markersize',14)
hold on

dessinpoint= true ;
nb_appel=0;

%xopt=Methoptim (FoncCout,x0, 'Nelder Matlab' )
xopt=Methoptim (FoncCout,x0, 'Pas Constant' );
%xopt=Methoptim (FoncCout,x0, 'Rech Lin',10^(-2) );
nb_appel 
