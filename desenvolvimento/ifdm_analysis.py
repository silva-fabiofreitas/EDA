import seaborn as sns
import matplotlib.pyplot as plt

class IFDMTemporalPlotter:
    def __init__(self, df, x='Ano', y='Quantidade', hue='C_IFDM', title='Evolução temporal por categoria', palette=None, figsize=(10, 6)):
        """
        Inicializa o plotador com os dados e configurações.

        Parâmetros:
        - df: DataFrame original com as colunas x e hue.
        - x: Nome da coluna para o eixo x (ex: 'Ano').
        - y: Nome da coluna para o eixo y (contagem agregada, ex: 'Quantidade').
        - hue: Coluna categórica para diferenciar as linhas.
        - title: Título do gráfico.
        - palette: Dicionário de cores por categoria, ou None para usar padrão.
        - figsize: Tamanho da figura (largura, altura).
        """
        self.df = df
        self.x = x
        self.y = y
        self.hue = hue
        self.title = title
        self.palette = palette or sns.color_palette("Set2")
        self.figsize = figsize
        self.grouped_df = None

    def prepare_data(self):
        """Agrupa os dados por x e hue, contando o número de registros."""
        self.grouped_df = self.df.groupby([self.x, self.hue], observed=True).size().reset_index(name=self.y)

    def plot(self):
        """Gera o gráfico de linha com os dados agregados."""
        sns.set_theme(style="white")
        self.prepare_data()

        plt.figure(figsize=self.figsize)
        ax = sns.lineplot(
            data=self.grouped_df,
            x=self.x,
            y=self.y,
            hue=self.hue,
            marker='o',
            palette=self.palette,
            linewidth=1.5
        )

        # Adiciona os rótulos de quantidade
        for _, row in self.grouped_df.iterrows():
            ax.annotate(
                text=str(row[self.y]),
                xy=(row[self.x], row[self.y]),
                xytext=(0, 8),
                textcoords='offset points',
                ha='center',
                fontsize=10,
                color='darkgrey'
            )

        plt.title(self.title)
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.tight_layout()
        plt.show()
