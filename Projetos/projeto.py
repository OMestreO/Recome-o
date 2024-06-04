from fpdf import FPDF

projeto = input("\nDescrição do projeto: ")
horas_estimadas = input("\nHoras estiamdas: ")
valor_hora = input("\nPreço da hora: ")
prazo = input("\nEm quanto tempo: ")
valor_total = int(horas_estimadas) * int(valor_hora)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)

pdf.text(115,145, projeto)
pdf.text(115,160, horas_estimadas)
pdf.text(115,175, valor_hora)
pdf.text(115,190, prazo)
pdf.text(115,205, str(valor_total))


pdf.output("projeto.pdf")
print("Projeto fucionando")
