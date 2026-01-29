CREATE TABLE despesas_consolidadas (
    cnpj VARCHAR(14),
    razao_social TEXT,
    ano INT,
    trimestre INT,
    valor_despesas DECIMAL(15,2)
);

CREATE TABLE operadoras (
    cnpj VARCHAR(14),
    registro_ans VARCHAR(20),
    modalidade TEXT,
    uf CHAR(2)
);

CREATE TABLE despesas_agregadas (
    razao_social TEXT,
    uf CHAR(2),
    total_despesas DECIMAL(15,2),
    media_trimestral DECIMAL(15,2),
    desvio_padrao DECIMAL(15,2)
);
