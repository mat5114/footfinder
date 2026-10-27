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

## Qualidade dos dados

Cada tênis tem um campo `data_quality` com o nível de confiança das especificações (`checked`, `high`, `medium` ou `low`) e a fonte. Os de confiança média e baixa são estimativas e precisam ser conferidos na ficha do fabricante antes do lançamento.

## Próximos passos

- Registrar o domínio e publicar a primeira versão
- Entrar nos programas de afiliado (Amazon Associates, AliExpress, Awin) e preencher `affiliate_links`
- Trocar as ilustrações pelas fotos oficiais fornecidas pelas lojas parceiras
