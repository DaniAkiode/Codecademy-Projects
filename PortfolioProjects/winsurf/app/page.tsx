import Link from 'next/link'
import { projects } from '@/lib/projects'
import ProjectCard from '@/components/ProjectCard'

export default function HomePage() {
  return (
    <>
      <section className="container mx-auto px-4 py-20">
        <div className="grid md:grid-cols-2 gap-10 items-center">
          <div>
            <h1 className="text-4xl md:text-6xl font-bold tracking-tight">
              Hi, I'm <span className="text-brand">Your Name</span>
            </h1>
            <p className="mt-6 text-lg text-gray-600 max-w-prose">
              Frontend Developer crafting delightful web experiences with React, Next.js, and TypeScript.
            </p>
            <div className="mt-8 flex gap-4">
              <Link href="/projects" className="button-primary">View Projects</Link>
              <Link href="/contact" className="inline-flex items-center justify-center rounded-md border border-gray-300 px-5 py-2.5 font-medium hover:bg-gray-50 transition-colors">Contact Me</Link>
            </div>
          </div>
          <div className="relative">
            <div className="aspect-square rounded-2xl bg-gradient-to-br from-brand/20 to-transparent border border-brand/30" />
          </div>
        </div>
      </section>

      <section className="container mx-auto px-4 py-12">
        <div className="flex items-end justify-between">
          <h2 className="text-2xl md:text-3xl font-semibold">About</h2>
          <Link href="/about" className="text-brand hover:underline">Read more →</Link>
        </div>
        <p className="mt-4 text-gray-600 max-w-3xl">
          Passionate developer focused on building performant and accessible interfaces. I love working across the stack and turning ideas into products.
        </p>
      </section>

      <section className="container mx-auto px-4 py-12">
        <div className="flex items-end justify-between">
          <h2 className="text-2xl md:text-3xl font-semibold">Featured Projects</h2>
          <Link href="/projects" className="text-brand hover:underline">All projects →</Link>
        </div>
        <div className="mt-6 grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {projects.slice(0, 3).map((p) => (
            <ProjectCard key={p.slug} project={p} />
          ))}
        </div>
      </section>
    </>
  )
}
