"use client";

import Board from "@/components/Board";
import { notFound } from "next/navigation";
import { useEffect, useState } from "react";
import { getBoards } from "@/services/api";
import { BoardData } from "@/types/board";

export default function Boards() {
    const [data, setData] = useState<BoardData[]>([]);
    const [error, setError] = useState<boolean>(false);

    useEffect(() => {
        const fetchBoards = async () => {
            try {
                const response = await getBoards()
                setData(response.data)
            } catch (error)
            {
                setError(true)
            }
        }
        fetchBoards();
    }, [])
    

    if (error) return notFound()
    return (
        <>
            {data.length !== 0 && (
                <>
                    <h1>Boards</h1>
                    {data.map((board) => (
                        <Board
                            key={board.board_id}
                            id={board.board_id}
                            name={board.name}
                            description={board.description}
                        />
                    ))}
                </>
            )}
        </>
    );
}
