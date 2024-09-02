# **Extrator de Tabelas**

## Descrição

**Extrator de Tabelas** é um script Python desenvolvido para extrair tabelas de arquivos PDF.

Utilizando as bibliotecas `tabula-py`, `pandas` e `jpype1`, o script processa PDFs e converte as tabelas contidas nesses documentos em ".csv", facilitando análises e manipulações posteriores.

## Bibliotecas Utilizadas

- **jpype1**: Permite a execução de código Java a partir do Python, necessária para o funcionamento do `tabula-py`.
- **tabula-py**: Interface simples para a biblioteca Tabula em Java, que permite a extração de tabelas de arquivos PDF.
- **pandas**: Utilizada para processar e armazenar as tabelas extraídas.

## Requisitos

Antes de executar o script, certifique-se de que as seguintes bibliotecas estão instaladas. Execute o seguinte comando para instalá-las:

```bash
pip install tabula-py pandas jpype1
```

Além disso, o tabula-py requer que o Java Runtime Environment (JRE) esteja instalado em seu sistema.

### Executando a Extração

Altere o diretório para o local em que consta o arquivo a ser editado e execute o script

As tabelas extraídas são retornadas como um arquivo ".csv"  que pode ser manipulado conforme necessário.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests no repositório GitHub do projeto.

## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
