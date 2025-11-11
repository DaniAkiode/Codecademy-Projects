import Link from 'next/link'

export default function Footer() {
  return (
    <footer className="border-t py-8 text-sm text-gray-600">
      <div className="container mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-4">
        <p>© {new Date().getFullYear()} Your Name. All rights reserved.</p>
        <div className="flex gap-4">
          <Link href="/about" className="hover:text-gray-900">About</Link>
          <Link href="/projects" className="hover:text-gray-900">Projects</Link>
          <Link href="/contact" className="hover:text-gray-900">Contact</Link>
        </div>
      </div>
    </footer>
  )
}
