import Link from "next/link";
import "./globals.css";

export const metadata = {
  title: "DROIX Benchmarks Portal",
  description: "Internal benchmark import and comparison portal"
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="shell">
          <header className="topbar">
            <Link href="/" className="brand">
              DROIX Benchmarks
            </Link>
            <nav className="nav" aria-label="Primary navigation">
              <Link href="/products">Products</Link>
              <Link href="/compare">Compare</Link>
              <Link href="/controls">Benchmark Controls</Link>
              <Link href="/aliases">Alias Review</Link>
            </nav>
          </header>
          <main className="page">{children}</main>
        </div>
      </body>
    </html>
  );
}
