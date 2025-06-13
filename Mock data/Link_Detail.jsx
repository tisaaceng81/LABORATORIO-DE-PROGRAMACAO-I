
    'use client';

import { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import { Box, Typography, Divider, CircularProgress } from '@mui/material';
import { RadarChart, Gauge } from '@mui/x-charts';

export default function LinkDetail() {
    const { id } = useParams();
    const [link, setLink] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchDadosDoLink = async () => {
            try {
                const response = await fetch('http://127.0.0.1:5000/api/links');
                if (!response.ok) {
                    throw new Error('Falha ao conectar ao servidor.');
                }
                const todosOsLinks = await response.json();
                const linkAtual = todosOsLinks.find(
                    (l) => l.nome.toLowerCase() === decodeURIComponent(id).toLowerCase()
                );
                setLink(linkAtual);
            } catch (err) {
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };
        fetchDadosDoLink();
    }, [id]);

    if (loading) return <Box sx={{ p: 4 }}><CircularProgress /> Carregando...</Box>;
    if (error) return <Box sx={{ p: 4 }}><Typography color="error">{error}</Typography></Box>;
    if (!link) return <Box sx={{ p: 4 }}><Typography color="error">Link não encontrado!</Typography></Box>;

    const { nome, avaliacao, classificacao, criterios } = link;
    const rotulosDosCriterios = ['Desempenho', 'Design', 'Usabilidade', 'Segurança', 'SEO'];
    const valoresDosCriterios = [
        criterios.desempenho, criterios.design, criterios.usabilidade, 
        criterios.seguranca, criterios.seo
    ];

    return (
        <Box sx={{ maxWidth: 900, margin: '0 auto', p: 4 }}>
            <Typography variant="h3">{nome}</Typography>
            <Typography variant="subtitle1">Classificação #{classificacao}</Typography>
            {/* O resto do seu JSX de exibição aqui... */}
            <Gauge value={avaliacao * 20} /* ... */ />
            <RadarChart series={[{ data: valoresDosCriterios, label: nome }]} /* ... */ />
        </Box>
    );
}
