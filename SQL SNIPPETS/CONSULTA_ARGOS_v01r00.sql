WITH base AS (
    SELECT
        numero_documento
        , card_id
        , LEFT(mask, 6) AS bin
        , (authorization_data::date + authorization_hora::time) AS ts_authorization
        , authorization_response
        , action_reason
        , authorization_valor
        , authorization_modalidade
        , estabelecimento_nome
        , authorization_mcc
    FROM schema.tb_assunto
    WHERE 1=1
        AND authorization_data >= '2025-09-01'
        AND authorization_data <= '2026-09-01'
        AND numero_documento IS NOT NULL
        AND authorization_hora IS NOT NULL
        AND authorization_response IN ('aprovada', 'reprovada')
        AND MOD(ABS(FNV_HASH(numero_documento)), {N_SHARDS}) = {k}
)
, seq AS (
    SELECT
        numero_documento
        , authorization_response
        , action_reason AS action_reason_reprovada
        , LEAD(action_reason) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS action_reason_aprovada
        , ts_authorization
        , LEAD(ts_authorization) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS ts_aprovada
        , authorization_valor AS valor_reprovada
        , LEAD(authorization_valor) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS valor_aprovada
        , authorization_modalidade AS canal_reprovada
        , LEAD(authorization_modalidade) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS canal_aprovada
        , bin AS bin_reprovada
        , LEAD(bin) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS bin_aprovada
        , estabelecimento_nome AS estabelecimento_reprovada
        , authorization_mcc AS tipo_estabelecimento_reprovada
        , LEAD(estabelecimento_nome) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS estabelecimento_aprovada
        , LEAD(authorization_mcc) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS tipo_estabelecimento_aprovada
        , card_id AS card_id_reprovada
        , LEAD(card_id) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS card_id_aprovada
        , LEAD(authorization_response) OVER (
            PARTITION BY numero_documento
            ORDER BY ts_authorization, card_id
          ) AS prox_resposta
    FROM base
)
SELECT
    numero_documento
    , action_reason_reprovada
    , action_reason_aprovada
    , ts_authorization AS ts_reprovada
    , ts_aprovada
    , DATEDIFF(second, ts_authorization, ts_aprovada) AS segundos_entre
    , valor_reprovada
    , valor_aprovada
    , canal_reprovada
    , canal_aprovada
    , bin_reprovada
    , bin_aprovada
    , estabelecimento_reprovada
    , tipo_estabelecimento_reprovada
    , estabelecimento_aprovada
    , tipo_estabelecimento_aprovada
    , card_id_reprovada
    , card_id_aprovada
FROM seq
WHERE 1=1
    AND authorization_response = 'reprovada'
    AND prox_resposta = 'aprovada';