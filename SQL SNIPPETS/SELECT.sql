-- CÁLCULO --> IDADE HOJE
SELECT
    nome
    , nascimento_data
    , DATEDIFF(year, cliente_nascimento_data, CURRENT_DATE)
        - CASE
            WHEN TO_CHAR(CURRENT_DATE, 'MMDD')
                 < TO_CHAR(cliente_nascimento_data, 'MMDD')
            THEN 1
            ELSE 0
    END AS idade_hoje
FROM
    schema.tb_assunto
WHERE 1=1
    AND idade_hoje >= 18
--    AND idade_hoje BETWEEN 30 AND 45
    AND cliente_estado_civil IN ('solteiro(a)', 'não mapeado')
    AND cliente_endereco_estado NOT IN ('sp', 'rj')
--    AND CAST(cliente_telefone_movel AS VARCHAR) LIKE '%992030209'
    AND cliente_telefone_movel IN (
        5531992030209,
        553192030209,
        31992030209,
        3192030209
    )
LIMIT 1000;