'use client';

import { useParams } from 'next/navigation';
import { Box, Typography, Divider } from '@mui/material';
import { RadarChart, Gauge } from '@mui/x-charts';

// Função para criar dados de exemplo para teste.
function gerarLinksDeExemplo(quantidade) {
    const listaDeLinks = [];
    for (let i = 1; i <= quantidade; i++) {
        listaDeLinks.push({
            nome: `Site Exemplo ${i}`,
            avaliacao: parseFloat((Math.random() * 4 + 1).toFixed(1)), // Nota de 1.0 a 5.0
            classificacao: i,
            criterios: {
                desempenho: parseFloat((Math.random() * 5).toFixed(1)),
                design: parseFloat((Math.random() * 5).toFixed(1)),
                usabilidade: parseFloat((Math.random() * 5).toFixed(1)),
                seguranca: parseFloat((Math.random() * 5).toFixed(1)),
                seo: parseFloat((Math.random() * 5).toFixed(1)),
            }
        });
    }
    return listaDeLinks;
}


// O nome do componente também foi traduzido de "LinkDetail" para "DetalheDoLink"
export default function DetalheDoLink() {
    const { id } = useParams();
    
    // Usamos a nossa função para gerar 10 links de exemplo
    const links = gerarLinksDeExemplo(10);

    // Encontra o link específico na lista
    const link = links.find((l) => l.nome.toLowerCase() === decodeURIComponent(id as string).toLowerCase());

    if (!link) {
        return (
            <Box sx={{ p: 4 }}>
                <Typography variant="h4" color="error">
                    Link não encontrado!
                </Typography>
                <Typography variant="body1">
                    Tente um nome como "Site Exemplo 1", "Site Exemplo 2", etc.
                </Typography>
            </Box>
        );
    }

    // Desestruturamos as propriedades com seus novos nomes em português
    const { nome, avaliacao, classificacao, criterios } = link;

    const rotulosDosCriterios = ['Desempenho', 'Design', 'Usabilidade', 'Segurança', 'SEO'];
    const valoresDosCriterios = [
        criterios.desempenho,
        criterios.design,
        criterios.usabilidade,
        criterios.seguranca,
        criterios.seo,
    ];

    return (
        <Box sx={{ maxWidth: 900, margin: '0 auto', p: 4 }}>
            <Typography variant="h3" gutterBottom>
                {nome}
            </Typography>
            <Typography variant="subtitle1" gutterBottom>
                Classificação #{classificacao}
            </Typography>
            <Divider sx={{ my: 2 }} />

            <Typography variant="h6">Avaliação Geral</Typography>
            <Gauge
                value={avaliacao * 20} // convertendo a nota (0-5) para a escala do medidor (0-100)
                valueMax={100}
                startAngle={-110}
                endAngle={110}
                text={({ value }) => `${(value / 20).toFixed(1)} / 5.0`}
                width={300}
                height={150}
                sx={{ my: 3 }}
            />

            <Divider sx={{ my: 4 }} />

            <Typography variant="h6">Critérios Avaliados</Typography>
            <RadarChart
                series={[{ data: valoresDosCriterios, label: nome }]}
                height={400}
                width={400}
                axisAngleLabels={{ formatter: (i) => rotulosDosCriterios[i] }}
            />

            <Divider sx={{ my: 4 }} />

            <Box>
                {rotulosDosCriterios.map((rotulo, indice) => (
                    <Typography key={rotulo} variant="body1">
                        {rotulo}: {valoresDosCriterios[indice].toFixed(1)}
                    </Typography>
                ))}
            </Box>
        </Box>
    );
}
