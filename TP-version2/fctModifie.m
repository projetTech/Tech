function y=fctModifie(t)
global critere
global x
y=critere(x-t*Calgrad(critere,x));
end
