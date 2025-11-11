export const metadata = {
  title: 'About | Portfolio',
}

export default function AboutPage() {
  return (
    <section className="container mx-auto px-4 py-16">
      <h1 className="text-3xl md:text-4xl font-bold">About Me</h1>
      <div className="mt-6 space-y-4 container-prose">
        <p>
          I'm a frontend developer with a focus on building modern, performant, and accessible web applications. My toolkit includes React, Next.js, TypeScript, and Tailwind CSS.
        </p>
        <p>
          I enjoy collaborating with cross-functional teams, designing clean UI, and shipping features that users love.
        </p>
      </div>
    </section>
  )
}
