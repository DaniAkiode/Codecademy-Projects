import type { Project } from '@/components/ProjectCard'

export const projects: Project[] = [
  {
    slug: 'portfolio-site',
    title: 'Personal Portfolio',
    description: 'A modern responsive portfolio built with Next.js 14 and Tailwind CSS.',
    tags: ['Next.js', 'Tailwind', 'TypeScript'],
  },
  {
    slug: 'dashboard-ui',
    title: 'Dashboard UI',
    description: 'Reusable dashboard components and charts with great UX.',
    tags: ['React', 'Charts', 'UI'],
  },
  {
    slug: 'api-integration',
    title: 'API Integration Demo',
    description: 'Demonstrates fetching and caching data with modern React patterns.',
    tags: ['React', 'API', 'Caching'],
  },
]
