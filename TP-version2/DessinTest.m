
function DessinTest(FoncCout)

% pour les fonctions 2D : FoncJ1, FoncJ2 ....
 
X=-15:0.8:15;
  Y=X;
  ndes=length(X);
  for i=1:ndes
    for j=1:ndes
    P=[X(i);Y(j)];
    Z(i,j)=FoncCout(P);
    MX(i,j)=X(i);
    MY(i,j)=Y(j);
    end
  end
    figure(2)
     surf(MX,MY,Z)
     figure (1)
     contour(MX,MY,Z,40)
  hold on
  axis equal
