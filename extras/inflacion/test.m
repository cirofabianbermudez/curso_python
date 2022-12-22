clear; close all; clc;

data = readtable('indicadores.csv','Range','A6:B631');
data.Properties.VariableNames = {'anios' 'inflacion'};
t = datetime(data.anios,'InputFormat','yyyy/MM');
str1 = strcat("Inflaci\'on de ", data.anios{1}," a ", data.anios{end});
str2 = strcat(data.anios{1}," a ", data.anios{end});

plot(t,data.inflacion, 'k','LineWidth',1.5,'DisplayName',str2);
legend('Location','northeast','Interpreter','latex','FontSize', 12);
ylim([ min(data.inflacion) max(data.inflacion)*1.05]);
grid on; grid minor;

title(str1,'Interpreter','latex'); 
xlabel('A\~nos','Interpreter','latex'); 
ylabel('Niveles','Interpreter','latex');
set(gca,'TickLabelInterpreter','latex', 'FontSize', 12);
