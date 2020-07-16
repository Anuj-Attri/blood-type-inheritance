from functions import punnett, parser
from plot import bar_plot

parents = [input("Enter Parent 1's blood type: "), input("Enter Parent 2's blood type: ")]

blood, rh = parser(parents)

gene_dict = {
  "A" : ["A", "A", "A", "O"],
  "B" : ["B", "B", "B", "O"],
  "O" : ["O", "O"],
  "AB": ["A", "B"]
}

rh_dict = {
	"+" : ["+","+","+", "-"],
	"-" : ["-" , "-"]
}

blood_prob = punnett(gene_dict[blood[0]], gene_dict[blood[1]])
rh_prob = punnett(rh_dict[rh[0]], rh_dict[rh[1]])

# print(blood_prob, rh_prob)

bar_plot(blood_prob, title="Alleles")
bar_plot(rh_prob, title = "Rhesus Factor")

