import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "@styles/globals.scss";

const InterFont = Inter({ subsets: ["latin"], weight: ["400", "600"] });

export const metadata: Metadata = {
    title: "Anon Forum",
};

export default function RootLayout({
    children,
}: Readonly<{
    children: React.ReactNode;
}>) {
    return (
        <html lang="en">
            <head>
                <link
                    rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
                ></link>
            </head>
            <body className={InterFont.className}>
                {children}
            </body>
        </html>
    );
}
