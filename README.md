# Footfinder

Quiz que recomenda tênis de corrida. A pessoa responde só com toques (objetivo, volume, distância, peso, pisada, largura do pé, orçamento) e recebe até 12 tênis, no máximo 2 por marca, com links de afiliado.

- Catálogo com 513 tênis de 30 marcas, incluindo marcas chinesas (Li-Ning, Anta, Xtep, 361° e outras)
- Perguntas adaptativas: cada resposta muda o título, as opções e quais perguntas aparecem depois
- Interface em inglês, português, espanhol, francês, alemão e italiano
- Ilustração de cada tênis gerada a partir da altura do solado e do drop reais, até as fotos das lojas parceiras estarem disponíveis

## Estrutura

```
data/running_shoes.json          catálogo completo (gerado)
scripts/catalog/data_western.py  dados das marcas ocidentais e nacionais
scripts/catalog/data_china.py    dados das marcas chinesas
scripts/catalog/build_catalog.py gera data/running_shoes.json
scripts/build_site.py            gera docs/ a partir do catálogo e do template
src/footfinder.template.html     página (HTML, CSS e JS em um arquivo)
docs/index.html                  site pronto para publicar
```

## Como gerar

```bash
python3 scripts/catalog/build_catalog.py   # só quando mudar os dados dos tênis
python3 scripts/build_site.py
```

Depois abra `docs/index.html` no navegador.

## Como publicar

O site fica na pasta `docs/`, que o GitHub Pages publica direto:

1. No repositório, abra **Settings → Pages**.
2. Em **Build and deployment → Source**, escolha **Deploy from a branch**.
3. Em **Branch**, escolha `main` e a pasta `/docs`, e clique em **Save**.

Em um ou dois minutos o site fica em `https://mat5114.github.io/footfinder/`.

A pasta `docs/` também funciona em Netlify, Vercel ou Cloudflare Pages sem configuração extra.

## Fotos e links do AliExpress

O script `scripts/aliexpress_fetch.py` busca cada tênis de marca chinesa na API de afiliados do AliExpress e salva a foto, o seu link de afiliado e o preço em `data/aliexpress.json`. O site mostra a foto real no lugar da ilustração e o botão do AliExpress vira link. Marcas ocidentais ficam de fora de propósito: no AliExpress elas costumam ser falsificadas.

As chaves nunca ficam no código. Elas são guardadas como segredos do repositório:

1. Em **Settings → Secrets and variables → Actions**, clique em **New repository secret** e crie três segredos: `ALIEXPRESS_APP_KEY`, `ALIEXPRESS_APP_SECRET` e `ALIEXPRESS_TRACKING_ID`.
2. Em **Actions**, abra **Update AliExpress photos and links** e clique em **Run workflow**.

O processo roda de novo toda segunda-feira para atualizar fotos, links e preços.

Depois de cada execução, confira `data/aliexpress_review.csv`. Se um tênis foi ligado ao anúncio errado, coloque o link ou o ID do anúncio certo em `data/aliexpress_overrides.json`, por exemplo `{"li-ning-red-hare-9-ultra": "https://www.aliexpress.com/item/1005001234567890.html"}`. Para nunca linkar um tênis, use `null`.

## Lojas da Awin (Nike BR, Netshoes, SportsShoes...)

O script `scripts/awin_fetch.py` baixa o feed de produtos de cada loja que aprovou você na Awin, encontra os tênis do catálogo e salva, por tênis, o link de afiliado, o preço e as fotos em `data/awin.json`. As fotos viram recortes sem fundo, e o resultado mostra um botão para cada loja, com as do país do visitante primeiro.

Configuração, em **Settings → Secrets and variables → Actions**:
- `AWIN_API_TOKEN`: o token de ui.awin.com/awin-api.
- `AWIN_PUBLISHER_ID`: o seu ID de publisher (opcional).

O resumo de cada execução mostra as lojas aprovadas, as que ainda estão em análise e quantos tênis foram encontrados em cada uma. Lojas sem o feed novo da Awin aparecem como "no Enhanced Feed".

## Links da Amazon

O botão da Amazon leva para a busca pelo nome do tênis na Amazon, com o seu código de afiliado. Não precisa da API.

Para ligar, coloque o seu Tracking ID em `data/amazon.json` (por exemplo `"tag": "footfinder-20"`) e, se o cadastro não for na amazon.com, troque `"store"` (por exemplo `"amazon.es"`). Depois rode `python3 scripts/build_site.py`.

As fotos da Amazon só podem vir pela API (liberada depois das primeiras vendas). Até lá, os tênis sem foto do AliExpress continuam com o desenho.

## Qualidade dos dados

Cada tênis tem um campo `data_quality` com o nível de confiança das especificações (`checked`, `high`, `medium` ou `low`) e a fonte. Os de confiança média e baixa são estimativas e precisam ser conferidos na ficha do fabricante antes do lançamento.

## Próximos passos

- Registrar o domínio e publicar a primeira versão
- Entrar nos programas de afiliado (Amazon Associates, AliExpress, Awin) e preencher `affiliate_links`
- Trocar as ilustrações pelas fotos oficiais fornecidas pelas lojas parceiras
