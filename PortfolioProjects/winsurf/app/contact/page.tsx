import Link from 'next/link'

export const metadata = {
  title: 'Contact | Portfolio',
}

export default function ContactPage() {
  return (
    <section className="container mx-auto px-4 py-16">
      <h1 className="text-3xl md:text-4xl font-bold">Get in touch</h1>
      <p className="mt-4 text-gray-600 max-w-prose">I'd love to hear from you. The best way to reach me is via email.</p>
      <div className="mt-8">
        <Link href="mailto:you@example.com" className="button-primary">Email me</Link>
      </div>
    </section>
  )
}
