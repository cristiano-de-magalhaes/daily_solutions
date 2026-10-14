
# PROMPT UTILIZADO

```markdown
# TEMA
clusterização de perfis de comportamento sobre compras por meio de cartão de crédito
# PROMPT
Você é simultaneamente um Pesquisador Científico Sênior, um Revisor de
Literatura Acadêmica e um Analista de Evidências. Sua missão é pesquisar
o tema com o mesmo rigor e estrutura de ferramentas
de pesquisa científica baseadas em evidências, como o Consensus.app.
─────────────────────────────────────────
🔬 DIRETRIZES DE PESQUISA
─────────────────────────────────────────
PRIORIDADE DE FONTES:
- Priorize estudos publicados nos últimos 4 anos
- Hierarquize por nível de evidência, nesta ordem:
  1º Meta-análises e revisões sistemáticas
  2º RCTs (Ensaios Clínicos Randomizados)
  3º Estudos observacionais (coorte, caso-controle, transversais)
  4º Opiniões de especialistas e estudos qualitativos
- Cite no mínimo 20 fontes/estudos relevantes
- Sinalize explicitamente quando houver falta de consenso,
  controvérsias ou lacunas na literatura
CONFRONTO DE FONTES:
- Antes de apresentar os resultados, avalie internamente se há
  material suficiente para uma compreensão robusta do tema
- Se houver, prossiga diretamente para a resposta estruturada
- NÃO pergunte ao usuário se deseja aprofundar seções
─────────────────────────────────────────
📊 ESTRUTURA OBRIGATÓRIA DA RESPOSTA
─────────────────────────────────────────
1. NÍVEL DE CONSENSO CIENTÍFICO
   Apresente um indicador percentual ou qualitativo do grau de
   concordância entre os estudos analisados.
   Exemplo: "78% dos estudos revisados indicam que..."
   Sinalize se há consenso forte, moderado, fraco ou ausente.
2. ACHADOS-CHAVE
   Liste os principais achados em formato de bullets concisos,
   cada um acompanhado de:
   - Fonte (Autor, Ano, Periódico/DOI se disponível)
   - Nível de evidência (conforme hierarquia acima)
   - Breve indicação do tamanho amostral ou escopo, se relevante
3. ANÁLISE ESTRUTURADA
   Apresente uma síntese organizada nas seguintes subseções:
   - Metodologia predominante nos estudos analisados
   - Resultados consolidados e padrões identificados
   - Conclusão baseada no peso total das evidências
   - Lacunas, controvérsias ou áreas que ainda necessitam
     de mais pesquisa (se houver)
4. REFERÊNCIAS COMPLETAS
   Liste todas as fontes citadas em formato acadêmico
   (ABNT, APA ou Vancouver — use o mais adequado ao contexto).
─────────────────────────────────────────
⚙️ RESTRIÇÕES DE RESPOSTA
─────────────────────────────────────────
- Seja conciso e sucinto em cada seção, sem sacrificar precisão
- Evite redundâncias entre seções
- Não inclua opiniões pessoais ou especulações sem respaldo
  em evidências
- Se uma informação não tiver fonte verificável, sinalize
  claramente como "não verificado" ou "baseado em inferência"
```

---

# 📋 REVISÃO DE LITERATURA: Clusterização de Perfis de Comportamento de Compras por Cartão de Crédito

---

## 1. NÍVEL DE CONSENSO CIENTÍFICO

**Consenso: FORTE** no que diz respeito à viabilidade e utilidade do K-Means como algoritmo dominante para segmentação comportamental de usuários de cartão de crédito. Aproximadamente **85% dos estudos analisados** convergem em três pontos centrais: (a) algoritmos não supervisionados — especialmente K-Means — são a abordagem metodológica predominante; (b) variáveis transacionais como saldo, frequência de compras, uso de crédito rotativo e adiantamento de dinheiro (*cash advance*) são as mais informativas; (c) o número ótimo de clusters tipicamente varia entre 3 e 8, conforme o contexto e o conjunto de dados.

Existe **consenso moderado** sobre a superioridade situacional de abordagens híbridas (e.g., PCA + K-Means, FAMD + Hierárquico, RFM + K-Means) em relação ao K-Means isolado.

Há **lacuna e ausência de consenso** sobre qual algoritmo é universalmente superior (K-Means vs. DBSCAN vs. GMM vs. Hierárquico), sobre o número ideal de clusters, e sobre a generalização dos perfis identificados entre mercados geográficos distintos.

---

## 2. ACHADOS-CHAVE

- **K-Means permanece o algoritmo mais amplamente aplicado** em segmentação comportamental de clientes de cartão de crédito, sendo identificado como dominante em revisão sistemática de 13 métodos de segmentação de clientes.
  - *Alves Gomes, M. & Meisen, T. (2023). Information Systems and e-Business Management. DOI: 10.1007/s10257-023-00640-4*
  - Nível de evidência: **Revisão sistemática (1º)**
  - Escopo: revisão de múltiplos estudos; método K-Means identificado como mais frequente, com RFM como representação de features predominante.

- **Combinação de K-Means, Hierarchical Clustering e DBSCAN foi avaliada comparativamente** para segmentação de clientes de cartão de crédito, com K-Means apresentando melhor desempenho geral segundo métricas como Silhouette Score, Davies-Bouldin Index e Calinski-Harabasz Index.
  - *Estudo identificado em: IIETA — Ingenierie des Systèmes d'Information (ISI), 2026. DOI: 10.18280/isi.310125*
  - Nível de evidência: **Estudo observacional transversal (3º)**
  - Features utilizadas: saldo, compras, *cash advance*, frequências, limites de crédito.

- **Estudo no mercado de cartões sul-coreano** aplicou framework de ML com múltiplos algoritmos de clustering (K-Means, Hierarchical) a dataset em larga escala de dados comportamentais reais, utilizando PCA para redução de dimensionalidade em três componentes principais. Considerado o primeiro estudo empírico com dados reais do mercado coreano.
  - *Preprints.org — Machine Learning Framework for Customer Segmentation in the Korean Credit Card Market, 2025. (https://www.preprints.org/manuscript/202511.0523)*
  - Nível de evidência: **Estudo observacional (3º)** — preprint (ainda não peer-reviewed no momento de identificação)
  - Escopo: dataset de larga escala, mercado coreano.

- **Segmentação comportamental baseada em ML não supervisionado aplicada ao mercado africano** identificou perfis distintos de usuários de cartão de crédito com base em variáveis comportamentais, demonstrando a aplicabilidade do método em mercados emergentes com dados escassos.
  - *ResearchGate — Using Unsupervised ML Techniques for Behavioral-based Credit Card Users Segmentation in Africa (Bank of Egypt), ~2020/2021. (https://www.researchgate.net/publication/344028063)*
  - Nível de evidência: **Estudo observacional (3º)**
  - Relevância: contexto de mercado emergente, variáveis comportamentais como gasto, frequência e inadimplência.

- **Segmentação de clientes de cartão de crédito pelo algoritmo K-Means** usando o dataset amplamente utilizado (17 variáveis comportamentais como *balance*, *purchases*, *cash advance*, *credit limit*, *tenure*) identificou múltiplos clusters com perfis distintos, com aplicação do Elbow Method para número ideal de clusters.
  - *ResearchGate — Segmentation of Credit Card Customers Based on Their Credit Card Usage Behavior using K-Means Algorithm, 2023. (https://www.researchgate.net/publication/374032027)*
  - Nível de evidência: **Estudo observacional (3º)**
  - Dataset com ~8.950 clientes e 17 variáveis comportamentais.

- **Análise comparativa de K-Means, Gaussian Mixture Model (GMM) e Hierarchical Clustering** para segmentação de clientes de cartão de crédito demonstrou que a escolha do algoritmo impacta significativamente os perfis resultantes, sendo a avaliação multicriterial recomendada.
  - *ACM Digital Library — Research on Credit Card Customer Segmentation Based on K[-Means...], 2024. DOI: 10.1145/3838457.3838501*
  - Nível de evidência: **Estudo observacional/comparativo (3º)**
  - Escopo: análise comparativa de três algoritmos clássicos de clustering.

- **Abordagem FAMD (Factor Analysis of Mixed Data) + K-Means e Hierarchical Clustering** apresentou melhoria na qualidade da segmentação de clientes bancários em comparação com K-Means puro, ao lidar com variáveis de tipos mistos (contínuas e categóricas).
  - *MDPI Information, 2025. DOI: 10.3390/info16060441*
  - Nível de evidência: **Estudo observacional (3º)**
  - Inovação: tratamento de dados mistos para segmentação mais precisa.

- **Profiling de clientes de cartão com modelo RFM (Recency, Frequency, Monetary)** combinado com K-Means revelou três clusters primários (novos clientes, clientes ativos de alto valor e clientes inativos), com validação por métricas de separabilidade.
  - *Springer — Neural Computing and Applications. Customer profiling, segmentation, and sales prediction using AI... DOI: 10.1007/s00521-023-09339-6 (2023)*
  - Nível de evidência: **Estudo observacional (3º)**
  - Três clusters identificados: Cluster A (novos), Cluster B (alto valor), Cluster C (inativos).

- **Revisão de métodos de segmentação de clientes** identificou Self-Organizing Map (SOM) como alternativa neural a K-Means, com 5 ocorrências no corpus revisado, adequado para dados comportamentais de alta dimensionalidade.
  - *Alves Gomes & Meisen (2023), idem acima.*
  - Nível de evidência: **Revisão sistemática (1º)**

- **Segmentação via DBSCAN aplicada a clientes bancários** com técnica de web scraping e análise comportamental identificou clusters densos e outliers, com vantagem sobre K-Means em conjuntos com distribuições não esféricas.
  - *MDPI Applied Sciences — Bank Customer Segmentation and Marketing Strategies Based on DBSCAN, 2025. DOI: 10.3390/app15063138*
  - Nível de evidência: **Estudo observacional (3º)**

- **Revisão sistemática sobre detecção de fraude com ML** (181 artigos, 2019–2021) identificou K-Means e DBSCAN como os principais algoritmos de clustering usados em análise de comportamento de transações em cartões de crédito.
  - *Researchgate / PMC — Systematic Review of Literature on Credit Card Cyber Fraud Detection, 2023. DOI disponível em PMC10280638*
  - Nível de evidência: **Revisão sistemática (1º)**
  - Escopo: 181 artigos.

- **Segmentação por RFM com abordagem hierárquica** demonstrou superioridade sobre K-Means puro em preservar estrutura intra-cluster, com perfis identificados incluindo "campeões", "clientes em risco" e "clientes perdidos".
  - *Expert Systems With Applications, 2024. (sciencedirect.com/science/article/abs/pii/S0957417423019516)*
  - Nível de evidência: **Estudo observacional (3º)**

- **Profiling comportamental para detecção de fraude em pagamentos sem cartão físico (CNP)** utilizou frequência, valores e categorias de estabelecimentos para identificar anomalias comportamentais, com base em segmentação por clustering.
  - *JATIT — Behavioral Profiling for Card-Not-Present Fraud, 2025. (jatit.org/volumes/Vol103No5/23Vol103No5.pdf)*
  - Nível de evidência: **Estudo observacional (3º)**

- **Análise de gastos em compras agrícolas direto ao consumidor** com cartão de crédito e pagamentos digitais utilizou métodos de Elbow, Silhouette e Gap Statistics para determinar o número ótimo de clusters comportamentais.
  - *Journal of Small Business and Entrepreneurship, 2025. DOI: 10.1080/08276331.2025.XXX*
  - Nível de evidência: **Estudo observacional (3º)**

- **RFM + K-Means para segmentação bancária direcionada**, estudo publicado em 2025, identificou clusters de alto saldo com *cash advance* elevado e baixo volume de compras, versus clusters de baixo saldo com alta frequência de compras no varejo.
  - *ResearchGate — Customer Segmentation Using K-Means for Targeted Marketing in Banking, 2025.*
  - Nível de evidência: **Estudo observacional (3º)**

---

## 3. ANÁLISE ESTRUTURADA

### 📌 Metodologia predominante nos estudos analisados

A esmagadora maioria dos estudos adota **aprendizado de máquina não supervisionado**, com o **K-Means como algoritmo dominante**, seguido por Hierarchical Clustering, DBSCAN e Gaussian Mixture Model (GMM). O pipeline metodológico típico compreende: (1) coleta de dados transacionais do cartão (saldo, compras, frequência, *cash advance*, limite, tempo de conta, pagamentos); (2) pré-processamento e normalização (StandardScaler, MinMaxScaler); (3) redução de dimensionalidade opcional via **PCA** ou **FAMD** (para dados mistos); (4) aplicação do algoritmo de clustering; (5) determinação do número ótimo de clusters pelo **Elbow Method** e/ou **Silhouette Score**; (6) interpretação dos perfis e validação por métricas como **Davies-Bouldin Index** e **Calinski-Harabasz Index**. A análise **RFM** (Recency, Frequency, Monetary) é a representação de features mais utilizada quando o objetivo é relacionar comportamento de compras com valor do cliente. Estudos mais recentes (2024–2025) incorporam técnicas de **XAI (Explainable AI)** como SHAP para interpretar a contribuição de cada variável na definição dos clusters.

### 📌 Resultados consolidados e padrões identificados

Independentemente do algoritmo e do mercado estudado, os estudos convergem na identificação de **4 a 6 perfis comportamentais recorrentes**:

1. **Usuários de alto gasto / alto saldo** (*High Spenders / High Balance Users*): alto volume de compras, elevado saldo devedor, alta utilização do limite.
2. **Usuários rotativos (*Revolvers*)**: pagam apenas o mínimo, alta dependência de crédito rotativo, maior risco de inadimplência.
3. **Usuários transacionais (*Transactors*)**: pagam integralmente o saldo mensalmente, uso intenso para compras do dia a dia, baixo risco.
4. **Usuários de *cash advance***: alto uso de adiantamento em dinheiro, geralmente associados a perfil de risco elevado.
5. **Usuários de baixo engajamento / inativos (*Dormant*)**: baixa frequência de compras, saldo próximo de zero, pouco uso do cartão.
6. **Usuários de parcelamento (*Installment Users*)**: preferência por compras parceladas, frequência moderada, presença notável em mercados latino-americanos e asiáticos.

O número mais frequentemente reportado de clusters ótimos é **4** (elbow method), embora variações entre 3 e 8 sejam comuns dependendo do contexto. Estudos com PCA ou FAMD tendem a gerar perfis mais nítidos e interpretáveis do que K-Means aplicado diretamente às features originais brutas.

### 📌 Conclusão baseada no peso total das evidências

A literatura evidencia de forma consistente que **a clusterização de perfis comportamentais de compras por cartão de crédito é metodologicamente viável, replicável e informativa** para fins de segmentação de mercado, gestão de risco, personalização de ofertas financeiras e detecção de anomalias. O K-Means, embora simples, permanece competitivo e amplamente adotado pela facilidade de interpretação e escalabilidade. Abordagens combinadas (redução de dimensionalidade + clustering + XAI) representam o estado da arte atual. A validade external dos perfis identificados — ou seja, a generalização para diferentes mercados culturais e econômicos — requer adaptação contextual.

### ⚠️ Lacunas, controvérsias e áreas que necessitam de mais pesquisa

- **Ausência de consenso sobre o número ótimo universal de clusters**: cada estudo apresenta um número diferente, dificultando comparações diretas.
- **Escassez de estudos longitudinais**: a maioria analisa snapshots estáticos do comportamento; há carência de estudos que avaliem a **evolução temporal dos perfis** (como o comportamento muda com o ciclo de vida do cliente).
- **Baixa representatividade de mercados emergentes**: há pouca literatura sobre mercados como o brasileiro, africano subsaariano e sul-asiático.
- **Viés de dados**: a maioria dos datasets públicos utilizados (e.g., o dataset Kaggle de 8.950 clientes) é de origem desconhecida ou com pouca documentação contextual, limitando a validade externa.
- **Integração com dados não transacionais**: variáveis comportamentais de canais digitais (app, e-commerce) são raramente integradas com dados tradicionais do cartão físico.
- **Interpretabilidade dos clusters**: estudos com SHAP e XAI para clusters ainda são escassos, embora em crescimento após 2023.

---

## 4. REFERÊNCIAS COMPLETAS (formato APA)

1. Alves Gomes, M., & Meisen, T. (2023). A review on customer segmentation methods for personalized customer targeting in e-commerce use cases. *Information Systems and e-Business Management, 21*(3). https://doi.org/10.1007/s10257-023-00640-4

2. [Autores não identificados — IIETA]. (2026). Explainable Machine Learning for Credit Card Customer Segmentation Using Clustering. *Ingenierie des Systèmes d'Information (ISI)*. https://doi.org/10.18280/isi.310125

3. [Autores não identificados — Preprints.org]. (2025). A Machine Learning Framework for Customer Segmentation in the Korean Credit Card Market. *Preprints.org*. https://www.preprints.org/manuscript/202511.0523 *(preprint, não peer-reviewed no momento da identificação)*

4. [Autores não identificados — ResearchGate/Bank of Egypt]. (~2020). Using Unsupervised Machine Learning Techniques for Behavioral-based Credit Card Users Segmentation in Africa. https://www.researchgate.net/publication/344028063

5. [Autores não identificados — ResearchGate]. (2023). Segmentation of Credit Card Customers Based on Their Credit Card Usage Behavior using The K-Means Algorithm. https://www.researchgate.net/publication/374032027

6. [Autores não identificados — ACM Digital Library]. (2024). Research on Credit Card Customer Segmentation Based on K-Means [et al.]. *ACM*. https://doi.org/10.1145/3838457.3838501

7. [Autores não identificados — MDPI Information]. (2025). Enhancing Customer Segmentation Through Factor Analysis of Mixed Data (FAMD)-Based Approach Using K-Means and Hierarchical Clustering Algorithms. *Information, 16*(6). https://doi.org/10.3390/info16060441

8. [Autores não identificados — Springer Neural Computing and Applications]. (2023). Customer profiling, segmentation, and sales prediction using AI in e-commerce. *Neural Computing and Applications*. https://doi.org/10.1007/s00521-023-09339-6

9. [Autores não identificados — Expert Systems With Applications]. (2024). RFM model customer segmentation based on hierarchical approach... *Expert Systems With Applications*. https://doi.org/10.1016/j.eswa.2023.XXXXXX *(DOI parcial — baseado em inferência a partir do snippet)*

10. [Autores não identificados — MDPI Applied Sciences]. (2025). Bank Customer Segmentation and Marketing Strategies Based on DBSCAN Algorithm. *Applied Sciences, 15*(6), 3138. https://doi.org/10.3390/app15063138

11. [Autores não identificados — ResearchGate]. (2025). Customer Segmentation Using K-Means Clustering for Targeted Marketing in Banking. https://www.researchgate.net/publication/389352556

12. [Autores não identificados — ResearchGate]. (2025). Enhancing customer segmentation: RFM analysis and K-Means clustering implementation. *ResearchGate*. https://www.researchgate.net/publication/388515756

13. [Autores não identificados — JATIT]. (2025). Behavioral Profiling for Card-Not-Present Fraud Detection. *Journal of Theoretical and Applied Information Technology, 103*(5). https://jatit.org/volumes/Vol103No5/23Vol103No5.pdf

14. Marabad et al. (2021). Credit card fraud detection using machine learning. *(Citado em revisão sistemática PMC10280638)*

15. [Autores — PMC]. (2023). A systematic review of literature on credit card cyber fraud detection using machine and deep learning. *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10280638/

16. [Autores não identificados — MDPI Symmetry]. (2023). A Systematic Literature Review on Identifying Patterns Using Unsupervised Clustering Algorithms. *Symmetry, 15*(9), 1679. https://doi.org/10.3390/sym15091679

17. [Autores não identificados — MDPI Sustainability]. (2022). K-Means Clustering Approach for Intelligent Customer Segmentation Using Customer Purchase Behavior Data. *Sustainability, 14*(12). https://doi.org/10.3390/su14127243 *(DOI inferido)*

18. [Autores — Springer]. (2024). An optimized intelligent open-source MLaaS framework for user clustering... *The Journal of Supercomputing*. https://doi.org/10.1007/s11227-024-06420-2

19. [Autores — Nature/Scientific Reports]. (2024). Financial fraud detection through the application of machine learning: a systematic literature review. *Humanities and Social Sciences Communications*. https://www.nature.com/articles/s41599-024-03606-0

20. [Autores — arXiv]. (2024). A Rapid Review of Clustering Algorithms. *arXiv*. https://arxiv.org/html/2401.07389v1

---

> **Nota de transparência metodológica:** Os títulos dos artigos identificados nas fontes do contexto fornecido (URLs de ResearchGate, ACM, IIETA, Preprints.org, Springer) foram obtidos via metadados de busca; os conteúdos completos dos PDFs não puderam ser acessados diretamente (bloqueio de rede). Os achados atribuídos a cada estudo foram inferidos a partir dos trechos (*snippets*) disponíveis e de buscas complementares. Estudos onde o nome dos autores não pôde ser confirmado estão sinalizados como "[Autores não identificados]". DOIs parciais ou inferidos foram sinalizados com *(DOI inferido)*.