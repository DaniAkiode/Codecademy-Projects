import ProjectCard from '@/components/ProjectCard'
import { projects } from '@/lib/projects'

export const metadata = {
  title: 'Projects | Portfolio',
}

export default function ProjectsPage() {
  return (
    <section className="container mx-auto px-4 py-16">
      <h1 className="text-3xl md:text-4xl font-bold">Projects</h1>
      <div className="mt-8 grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map((p) => (
          <ProjectCard key={p.slug} project={p} />
        ))}
      </div>
    </section>
  )
}
