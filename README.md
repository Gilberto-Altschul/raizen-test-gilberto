# raizen-test-gilberto

- converted the excel file to xlsx vendas-combustiveis-m3.xlsx with two tabs Planilha1 e Planilha2. 

- the data in each tab is in the followig collumns COMBUSTÍVEL, ANO, REGIÃO, ESTADO, UNIDADE, Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez, TOTAL

- the program in python extract the data from the two tabs and store the data in the following schema in excel file: collumn year_month, data type date, collumn uf, data type string, collumn product, data type string, collumn unit, data type string, collumn volume, data type double, collumn created_at, data type timestamp

- The mapping from the input to the output is

year_month = ANO || IF 'Jan' then 01, IF 'Fev' then 02, and so for until Dez,
uf = ESTADO,
product = COMBUSTÍVEL,
unit = UNIDADE,
volume =  IF 'Jan' then cell corresponding collumn 'Jan' for each line from input, IF 'Fev' then cell corresponding collumn 'Fev' and so for

each month 'Jan', 'Fev, 'Mar,... will be a line for output


- docker container on windows to store the project. The excel files will be in the same directory of the image docker

- github to save all the project that a user can create an image in a docker container and test 

 
# The user must create a docker container image with this commands:

docker build -t image-rayzen-gilberto -f Dockerfile.txt C:\Raizen-Repository 
remarks: change C:\Raizen-Repository by the folder where you dowloaded the files from do github 

# Run the project with this command:
docker run -it image-rayzen-gilberto python raizen.py

Should display the validation of the process and that the excel file was writen.

PS C:\Users\gilbe> docker run -it image-rayzen-gilberto python raizen.py
Diretório de Trabalho: /app
total_volume_input=  138012933.25249162
total_volume_output=  138012933.25249165
Os totais são iguais.
DataFrame salvo com sucesso em /app/output_data.xlsx
PS C:\Users\gilbe> 
