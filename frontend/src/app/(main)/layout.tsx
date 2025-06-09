"use client";
import "@styles/globals.scss";
import style from "./layout.module.scss";
import Navigation from "@/components/Navigation";

export default function DashboardLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <>
            <header>
                <Navigation />
            </header>
            <main className={style.main}>{children}</main>
            <footer style={{ margin: "5em" }}></footer>
        </>
    );
}
