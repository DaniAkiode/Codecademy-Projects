import Link from 'next/link'

export type Project = {
  slug: string
  title: string
  description: string
  tags: string[]
}

export default function ProjectCard({ project }: { project: Project }) {
  return (
    <article className="group rounded-xl border p-5 hover:shadow-sm transition">
      <h3 className="text-lg font-semibold group-hover:text-brand">
        <Link href={`/projects#${project.slug}`}>{project.title}</Link>
      </h3>
      <p className="mt-2 text-gray-600">{project.description}</p>
      <ul className="mt-4 flex flex-wrap gap-2">
        {project.tags.map((t) => (
          <li key={t} className="text-xs rounded-full bg-gray-100 px-2.5 py-1 text-gray-700">{t}</li>
        ))}
      </ul>
    </article>
  )
}
