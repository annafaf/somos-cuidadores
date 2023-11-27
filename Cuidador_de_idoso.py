import tkinter as tk
from tkinter import messagebox


class Formulario:

    def __init__(self, root):
        self.root = root
        self.root.geometry("800x800")
        self.root.title("Formulário de Saúde")

        self.opcao_var = tk.StringVar()

        self.frame_principal = tk.Frame(self.root)
        self.frame_principal.pack()

        self.label_instrucao = tk.Label(self.frame_principal, text="Selecione uma opção:")
        self.label_instrucao.grid(row=0, column=0, pady=10)

        opcoes = ["Sou paciente", "Sou profissional da saúde", "Sou responsável", "Sou cuidador"]

        for i, opcao in enumerate(opcoes):
            radio_button = tk.Radiobutton(self.frame_principal, text=opcao, variable=self.opcao_var, value=opcao,
                                          command=self.abrir_formulario)
            radio_button.grid(row=i + 1, column=0)

    def abrir_formulario(self):
        opcao_selecionada = self.opcao_var.get()

        if opcao_selecionada == "Sou paciente":
            self.abrir_formulario_paciente()
        elif opcao_selecionada == "Sou profissional da saúde":
            self.abrir_formulario_profissional()
        elif opcao_selecionada == "Sou responsável":
            self.abrir_formulario_responsavel()
        elif opcao_selecionada == "Sou cuidador":
            self.abrir_formulario_cuidador()

    def validar_campos_preenchidos(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, tk.Checkbutton):
                if widget.get() == "":
                    return False
        return True

    def abrir_formulario_paciente(self):
        self.frame_principal.destroy()

        frame_paciente = tk.Frame(self.root)
        frame_paciente.pack()

        labels = ["* Nome completo", "* CPF do paciente", "* Data de nascimento", "* Gênero", "* E-mail",
                  "* Telefone", "* Endereço", "Enfermidades", "Consultas, exames, cirurgias", "* Tipo de convênio"]

        for i, label in enumerate(labels):
            tk.Label(frame_paciente, text=label).grid(row=i, column=0, pady=5)
            tk.Entry(frame_paciente).grid(row=i, column=1, pady=5)

        enviar_button = tk.Button(frame_paciente, text="Enviar", command=lambda: self.enviar_formulario(frame_paciente))
        enviar_button.grid(row=i + 1, column=0, columnspan=2, pady=10)

    def abrir_formulario_profissional(self):
        self.frame_principal.destroy()

        frame_profissional = tk.Frame(self.root)
        frame_profissional.pack()

        labels = ["* Nome completo", "* CPF do profissional", "* Número CRM", "* Gênero", "* E-mail",
                  "* Telefone", "* Endereço", "* Especialidade", "* Atende via plano de saúde", "* Atende via SUS"]

        for i, label in enumerate(labels):
            tk.Label(frame_profissional, text=label).grid(row=i, column=0, pady=5)
            if "Atende" in label:
                tk.Checkbutton(frame_profissional).grid(row=i, column=1, pady=5)
            else:
                tk.Entry(frame_profissional).grid(row=i, column=1, pady=5)

        enviar_button = tk.Button(frame_profissional, text="Enviar", command=lambda: self.enviar_formulario(frame_profissional))
        enviar_button.grid(row=i + 1, column=0, columnspan=2, pady=10)

    def abrir_formulario_responsavel(self):
        self.frame_principal.destroy()

        frame_responsavel = tk.Frame(self.root)
        frame_responsavel.pack()

        labels = ["* Nome completo", "* CPF", "* E-mail", "* Telefone", "* Endereço", "* Responsável legal por"]

        for i, label in enumerate(labels):
            tk.Label(frame_responsavel, text=label).grid(row=i, column=0, pady=5)
            tk.Entry(frame_responsavel).grid(row=i, column=1, pady=5)

        enviar_button = tk.Button(frame_responsavel, text="Enviar",
                                  command=lambda: self.enviar_formulario(frame_responsavel))
        enviar_button.grid(row=i + 1, column=0, columnspan=2, pady=10)

    def abrir_formulario_cuidador(self):
        self.frame_principal.destroy()

        frame_cuidador = tk.Frame(self.root)
        frame_cuidador.pack()

        labels = ["* Nome completo", "* Data de nascimento", "* CPF", "* Gênero", "* E-mail", "* Telefone",
                  "* Endereço", "Escolaridade", "Formação acadêmica", "Experiência profissional", "Local de atuação"]

        for i, label in enumerate(labels):
            tk.Label(frame_cuidador, text=label).grid(row=i, column=0, pady=5)
            tk.Entry(frame_cuidador).grid(row=i, column=1, pady=5)

        enviar_button = tk.Button(frame_cuidador, text="Enviar",
                                  command=lambda: self.enviar_formulario(frame_cuidador))
        enviar_button.grid(row=i + 1, column=0, columnspan=2, pady=10)

    def enviar_formulario(self, frame):
        if self.validar_campos_preenchidos(frame):
            messagebox.showinfo("Enviado", "Formulário enviado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")


if __name__ == "__main__":
    root = tk.Tk()
    formulario = Formulario(root)
    root.mainloop()
